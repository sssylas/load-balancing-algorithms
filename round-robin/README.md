# Round Robin Load Balancing

Round Robin distributes requests sequentially across available servers.

This example demonstrates:
- Even traffic distribution
- Lack of awareness of server performance
- How slower servers increase overall latency

Run:
```bash
python round_robin.py