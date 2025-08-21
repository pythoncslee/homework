#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 13:50:59 2025

@author: jacksonlee
"""

from ai_benchmark import AIBenchmark
import sys

def run_ai_benchmark():
    try:
        # Initialize the AI Benchmark
        benchmark = AIBenchmark()
        
        # Run the benchmark (use_verbose=True for detailed output)
        results = benchmark.run()
        
        # Print the results
        print("\nAI Benchmark Results:")
        print(f"AI Score: {results.ai_score}")
        print("\nDetailed Results:")
        for task, score in results.details.items():
            print(f"{task}: {score}")
            
    except Exception as e:
        print(f"Error running AI Benchmark: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Starting AI Benchmark...")
    run_ai_benchmark()
    print("Benchmark completed.")