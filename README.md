# 🧬 GA-Microservices-LoadBalancer

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

## 📌 Overview
This repository contains the Python-based simulation environment developed for the paper: **"Optimizing Response Time in Microservices Architecture Using Genetic Algorithms"**. 

The project implements a metaheuristic approach to dynamically balance workloads across heterogeneous microservice instances, aiming to minimize the overall system response time (Makespan). This dynamic routing strategy is specifically designed to integrate seamlessly into modern CI/CD pipelines and DevOps workflows, preventing system-level bottlenecks and SLA violations.

## 🚀 Key Features
* **Custom Genetic Algorithm:** Features elitism, Roulette Wheel selection, single-point crossover, and uniform mutation.
* **Heterogeneous Environment Simulation:** Accurately models the varying processing capacities of different service nodes.
* **DevOps Ready:** Lightweight and designed to re-optimize allocation arrays within milliseconds for real-time traffic routing.
* **Performance:** Demonstrates up to a 34.6% improvement in Makespan compared to static load balancing methods like Round Robin.

## ⚙️ How to Run
1. Ensure you have Python and `numpy` installed.
2. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/GA-Microservices-LoadBalancer.git](https://github.com/yourusername/GA-Microservices-LoadBalancer.git)
