from client import AiEvaluationCustomBenchmarkRunnerClient

def main():
    client = AiEvaluationCustomBenchmarkRunnerClient()
    res = client.run_benchmark_eval("./evals/realworld_agent_tasks.jsonl", "model_v1")
    print(f"Accuracy Score: {res['accuracy_score_pct']}% ({res['total_evals_passed']} passed)")
    print("Report:", res["benchmark_report"])

if __name__ == "__main__":
    main()
