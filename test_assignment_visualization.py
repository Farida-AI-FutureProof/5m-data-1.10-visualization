#!/usr/bin/env python3
"""
Quick test runner for assignment_visualization.py

Usage:
  python test_assignment_visualization.py
"""

from __future__ import annotations

import importlib


def main():
    mod = importlib.import_module("assignment_visualization")

    # Q1 should return (fig, axes, ax)
    fig, axes, ax = mod.q1_subplots_first_ax()
    assert fig is not None, "Q1: fig is None"
    assert axes is not None, "Q1: axes is None"
    assert ax is not None, "Q1: ax is None"

    # Sanity check: axes shape should be (2,2)
    assert axes.shape == (2, 2), f"Q1: expected axes shape (2,2), got {axes.shape}"

    # Q2-Q6: just verify functions exist (calling them will pop plots)
    for fn_name in [
        "q2_red_dashed_line",
        "q3_hist_30_bins",
        "q4_set_axis_labels",
        "q5_seaborn_barplot_avg_tip_per_day",
        "q6_seaborn_boxplot_total_bill_by_day",
    ]:
        fn = getattr(mod, fn_name, None)
        assert callable(fn), f"Missing or not callable: {fn_name}"

    print("✅ Basic checks passed.")
    print("If you want to visually verify plots, run: python assignment_visualization.py")


if __name__ == "__main__":
    main()
