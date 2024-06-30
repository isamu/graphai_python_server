#curl  -X POST -H "Content-Type: application/json" -d '{"inputs": "aa"}' http://localhost:8000/agents/echoAgent

# curl  -X POST -H "Content-Type: application/json" -d '{"inputs": ["1", "2"]}' http://localhost:8000/agents/copyAgent

curl  -X POST -H "Content-Type: application/json" -d '{"inputs": ["1", "2"]}' http://localhost:8000/agents/streamAgent
