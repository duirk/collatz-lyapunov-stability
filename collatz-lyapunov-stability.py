import gradio as gr
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

MAX_ITER = 10000
CACHE = {1: 0}

def collatz_next(n):
    if n % 2 == 0:
        return n // 2
    return 3*n + 1


def analyze_number(n):
    visited = set()
    sequence = []

    steps = 0
    max_value = n

    while n != 1 and steps < MAX_ITER:

        if n in visited:
            return {
                "cycle": True,
                "sequence": sequence
            }

        visited.add(n)
        sequence.append(n)

        n = collatz_next(n)

        max_value = max(max_value, n)
        steps += 1

    return {
        "cycle": False,
        "steps": steps,
        "max": max_value,
        "sequence": sequence
    }


def analisis_instituto_matematico(video_path):

    cap = cv2.VideoCapture(video_path)

    record_steps = 0
    record_seed = 0
    record_sequence = []

    cycle_found = False
    cycle_seed = None

    steps_distribution = []

    frame_count = 0

    while cap.isOpened() and frame_count < 100:

        ret, frame = cap.read()
        if not ret:
            break

        for _ in range(30):

            y = np.random.randint(0, frame.shape[0])
            x = np.random.randint(0, frame.shape[1])

            r, g, b = frame[y, x]

            n = int(r)*65536 + int(g)*256 + int(b) + 1

            result = analyze_number(n)

            if result["cycle"]:
                cycle_found = True
                cycle_seed = n
                break

            steps_distribution.append(result["steps"])

            if result["steps"] > record_steps:

                record_steps = result["steps"]
                record_seed = n
                record_sequence = result["sequence"]

        if cycle_found:
            break

        frame_count += 1

    cap.release()

    plt.style.use("seaborn-v0_8-whitegrid")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    if record_sequence:
        ax1.plot(record_sequence)
        ax1.set_yscale("log")
        ax1.set_title(f"Collatz trajectory (seed={record_seed})")
        ax1.set_ylabel("Value (log scale)")

    ax2.hist(steps_distribution, bins=40, color="green", alpha=0.7)
    ax2.set_title("Stopping time distribution")
    ax2.set_xlabel("Iterations")
    ax2.set_ylabel("Frequency")

    plt.tight_layout()

    plot_path = "collatz_analysis.png"
    plt.savefig(plot_path)

    df = pd.DataFrame({
        "steps": steps_distribution
    })

    csv_path = "collatz_data.csv"
    df.to_csv(csv_path, index=False)

    if cycle_found:
        conclusion = f"""
POTENTIAL COUNTEREXAMPLE FOUND

Seed: {cycle_seed}

A non-trivial cycle may exist.
Further mathematical verification required.
"""
    else:
        conclusion = f"""
COMPUTATIONAL VERIFICATION REPORT

Numbers tested: {len(steps_distribution)}

No divergent trajectories detected.
No cycles different from 4-2-1 detected.

Record stopping time: {record_steps}
Record seed: {record_seed}

Conclusion:
Evidence supports the Collatz behaviour but does NOT constitute a proof.
"""

    return conclusion, csv_path, plot_path


demo = gr.Interface(
    fn=analisis_instituto_matematico,
    inputs=gr.Video(),
    outputs=[
        gr.Textbox(label="Mathematical Report"),
        gr.File(label="Dataset"),
        gr.Image(label="Analysis Graphs")
    ],
    title="Collatz Counterexample Scanner"
)

demo.launch()
