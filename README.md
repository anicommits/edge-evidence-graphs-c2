# Edge Evidence Graphs for Spacecraft Command-and-Control Security: A Benchmark Audit on Synthetic Data

[![Conference](https://img.shields.io/badge/IEEE%20CCNC%202027-Accepted-brightgreen.svg)](https://ccnc2027.ieee-ccnc.org/)
[![Track](https://img.shields.io/badge/Workshop-IEEE%20STP--CPS%202027-blue.svg)](#)
[![Publisher](https://img.shields.io/badge/Publication-IEEE%20Xplore-red.svg)](https://ieeexplore.ieee.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Official repository containing the camera-ready LaTeX source, architectural figures, data macros, and manuscript PDF for:

> **Edge Evidence Graphs for Spacecraft Command-and-Control Security: A Benchmark Audit on Synthetic Data**  
> **Author:** Aniket Chakraborty (*The Heritage Academy, MAKAUT, Kolkata, India*)  
> **Accepted for publication in:** *Proceedings of the 2027 IEEE 24th Consumer Communications & Networking Conference (CCNC) — Workshop on Security, Trust, and Privacy for Cyber-Physical Systems (IEEE STP-CPS)*. To appear in **IEEE Xplore**.

---

## 📌 Abstract

Spacecraft command-and-control (C2) is a safety-critical cyber-physical system in which a cryptographically valid command can still be physically unsafe. We study SP-SP-GAT, a typed relational graph model of C2 that consumes per-edge telemetry indicators with applicability masks, together with a deterministic command gate that is specified but not yet implemented. On the synthetic SatSecGraph-1 benchmark (50 missions, 18 classes, five dataset seeds), the corrected model reaches $0.949 \pm 0.007$ Macro-F1 under a common training protocol, above graph baselines with bootstrap CIs excluding zero, while DeepSets is marginally higher and HistGradientBoosting is not distinguishable.

Replacing learned attention by uniform weights changes nothing detectable; the margin over graph baselines that use node features only in message passing is consistent with edge-aware message passing. An audit identified three implementation defects (an identically zero pooled feature, an attention softmax normalised over the whole graph, and premature early stopping); correcting the first two raises Macro-F1 from 0.657 to 0.949 (V0 to V2). Single features separate all 17 attack sublabels from plain nominal telemetry (17/17 at $\ge 86\%$ recall and $\le 1.5\%$ FPR), but a multi-feature static threshold monitor raises about 60% false alarms on benign disturbance episodes, against 8–21% for the corrected graph and set models.

---

## 📂 Repository Contents

```text
.
├── Edge_Evidence_Graphs_for_Spacecraft_Command_and_Control_Security__A_Benchmark_Audit_on_Synthetic_Data.pdf
│                                 # Camera-ready manuscript (IEEE format, 7 pages)
├── main.tex                      # Complete LaTeX camera-ready source
├── Fig1_final2.png               # Figure 1 architectural diagram (high-resolution PNG)
├── Fig1_final2.pdf               # Figure 1 architectural diagram (vector PDF)
├── fig1_final2.py                # Python generation script for Figure 1
├── tables/
│   ├── macros_final.tex          # LaTeX number macros with experimental provenance
│   ├── macros_final2.tex         # Extended experimental macros
│   ├── macros_final3.tex         # Recomputed ablation and bootstrap CI macros
│   ├── table_master_main.tex     # Master performance comparison table (Table III)
│   ├── table_ablation.tex        # Ablation study table (Table IV)
│   ├── table_single_feature_separability.tex # Single-feature audit table (Table V)
│   └── table_computational_cost.tex          # Model cost and latency table (Table VI)
├── .gitignore                    # TeX auxiliary file ignore rules
├── LICENSE                       # MIT License
└── README.md                     # Documentation and citation guide
```

---

## 🛠️ Compilation

The manuscript uses standard IEEE conference formatting (`IEEEtran`). You can compile the PDF directly:

```bash
# Using tectonic:
tectonic main.tex

# Or using pdflatex:
pdflatex main.tex
pdflatex main.tex
```

---

## 📖 Citation

```bibtex
@inproceedings{chakraborty2027edge,
  author    = {Chakraborty, Aniket},
  title     = {Edge Evidence Graphs for Spacecraft Command-and-Control Security: A Benchmark Audit on Synthetic Data},
  booktitle = {Proceedings of the 2027 IEEE 24th Consumer Communications \& Networking Conference (CCNC) - Workshop on Security Trust Privacy for Cyber-Physical Systems (STP-CPS)},
  year      = {2027},
  pages     = {1--7},
  publisher = {IEEE}
}
```

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
