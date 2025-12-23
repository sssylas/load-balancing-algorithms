# load-balancing-algorithms
The goal of this repository contains simple, hands-on Python examples of common load balancer algorithms used in networking and cloud environments.

The goal of the project is to explore:
- How different load balancing algorithms road traffic
- The tradeoffs and limitations of each approach
- Why algorithm choice matters when making a decision about performance, reliability, and scalability

Each implementation is intentionally minimal and observable with logging and timing included to the behavior and bottlenecks of certain algorithms visually able to see.

## Currently Implemented
- Round Robin

## Planned Implementation
- IP Hash
- Least Connections
- Least Response Time

## How to Use
Each algorithm will live in its own directory with:
- A python implementation
- A README explaining the algorithm
- Example output demonstrating real-world behavior of each algorithm

To run an example:
```bash
cd round-robin
python round-robin.py

