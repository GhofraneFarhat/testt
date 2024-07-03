# Plaspipe

Plaspipe is a bioinformatic pipeline for plasmid analysis. This pipeline integrates bioinformatic tools such as PlASgraph, Platon, and Plasbin-flow, providing a streamlined and efficient workflow for plasmid identification, classification, and binning.

## Table of Contents
- [Installation](#installation)
- [Pipeline Workflow](#pipeline-workflow)
- [Pipeline Prerequisites](#pipeline-prerequisites)
- [Usage](#usage)
- [Gurobi Solver Dependency](#gurobi-solver-dependency)

## Installation

Plaspipe is now available as a Conda package. To install:

```bash
conda create -n plaspipe_env -c conda-forge -c bioconda plaspipe
conda activate plaspipe_env
```

## Errors
```bash
Encountered problems while solving:
  - nothing provides requested gurobipy >=9.1.2
  - nothing provides requested spektral >=1.0.8

```
