# CarbonScale: Carbon-Aware GPU Autoscaling

**CarbonScale** is a Kubernetes-based approach to reducing the environmental impact of AI workloads. While traditional autoscalers are "carbon-blind," CarbonScale uses real-time grid intensity data to dynamically adjust GPU pod replicas.

## Key Findings
- **38% Carbon Reduction:** Achieved in high-volatility regions (Iowa, Virginia, Singapore).
- **Minimal Latency Hit:** <3% performance penalty.
- **Simplicity Wins:** Threshold-based policies outperformed complex RL models in real-world traces.

## How it Works
The system pings the **Electricity Maps API** every 60 seconds. It compares the current `gCO2eq/kWh` (grams of CO2 equivalent per kilowatt hour) against a user-defined threshold. 



## Repository Contents
- `/src`: Contains the core logic for the threshold-based scaling algorithm.
- `/k8s`: Sample Kubernetes Custom Resource Definition (CRD) for the operator.
