# GhatGPT CasaOS AppStore

Готовый локальный CasaOS AppStore для установки:

- Ollama с NVIDIA GPU и папкой моделей `/opt/ollama`.
- GhatGPT на порту `3000`.
- GhatGPT Monitor на порту `3420`.
- Отдельные установщики моделей Ollama.
- Общий установщик `Models All`.

## Порты

- GhatGPT: `http://192.168.0.238:3000`
- Ollama API: `http://192.168.0.238:11434`
- Monitor: `http://192.168.0.238:3420`

## Как использовать

1. Распаковать ZIP на сервер или положить ZIP туда, откуда CasaOS сможет добавить custom app store.
2. В CasaOS открыть App Store -> Add Source / Custom App Store.
3. Добавить этот репозиторий/zip.
4. Сначала установить `Ollama` или `GhatGPT Stack`.
5. Потом установить `GhatGPT` если не ставили stack.
6. Потом ставить модели по одной или `Models All`.

## Важно

- `/opt/ollama` не удалять: там модели.
- Для моделей нужен запущенный Ollama на `127.0.0.1:11434` / `192.168.0.238:11434`.
- Модельные приложения являются one-shot installer: контейнер скачивает модель, создаёт русский alias и завершается с кодом 0.
- Для доступа извне нужно открыть/пробросить порты на роутере: `3000`, `3420`, при необходимости `11434`.

## Модели в репозитории

- Qwen3.5 9B: base `qwen3.5:9b` -> alias `ru-qwen3.5:9b`
- Qwen3.6 27B: base `qwen3.6:27b` -> alias `ru-qwen3.6:27b`
- Gemma 4 E4B: base `gemma4:e4b` -> alias `ru-gemma4:e4b`
- Gemma 4 26B A4B: base `gemma4:26b` -> alias `ru-gemma4:26b`
- Nemotron 3 Nano 4B: base `nemotron-3-nano:4b, nvidia/nemotron-3-nano-4b:latest` -> alias `ru-nemotron-3-nano:4b`
- LFM2 24B A2B: base `lfm2:24b-a2b, lfm2:24b` -> alias `ru-lfm2:24b-a2b`
- GLM 4.7 Flash: base `glm-4.7-flash:latest, zai-org/glm-4.7-flash:latest` -> alias `ru-glm-4.7-flash:latest`
- GLM 4.6V Flash: base `zai-org/glm-4.6v-flash:latest, haervwe/GLM-4.6V-Flash-9B:latest` -> alias `ru-glm-4.6v-flash:latest`
- Devstral Small 2: base `devstral-small-2:latest, devstral:latest` -> alias `ru-devstral-small-2:latest`
- RNJ 1: base `rnj-1:latest, essentialai/rnj-1:latest` -> alias `ru-rnj-1:latest`
- Ministral 3 14B Reasoning: base `TechyShishy/ministral-3:14b-reasoning-2512-q4_K_M, mistralai/ministral-3-14b-reasoning:latest` -> alias `ru-ministral-3:14b-reasoning`
- OlmoCR 2 7B: base `richardyoung/olmocr2:7b-q8, allenai/olmocr-2-7b:latest` -> alias `ru-olmocr2:7b`
- Phi 4 Reasoning Plus: base `phi4-reasoning:plus, phi4:latest` -> alias `ru-phi4-reasoning:plus`
- GPT OSS 20B: base `gpt-oss:20b, openai/gpt-oss-20b:latest` -> alias `ru-gpt-oss:20b`
- Hermes 3 8B: base `hermes3:8b, hermes3:latest, hermes:latest` -> alias `ru-hermes3:8b`
- Mistral Large: base `mistral-large:latest` -> alias `ru-mistral-large:latest`
- Nemotron 3 Super: base `nemotron-3-super:latest` -> alias `ru-nemotron-3-super:latest`
- Photo Gemma3 27B: base `gemma3:27b` -> alias `ru-photo-gemma3:27b`
- Yarn Mistral 7B 128K: base `yarn-mistral:7b-128k, ru-yarn-mistral:7b-128k` -> alias `ru-yarn-mistral:7b-128k`
- Qwen3 30B: base `qwen3:30b` -> alias `ru-qwen3:30b`
- Qwen3 32B: base `qwen3:32b` -> alias `ru-qwen3:32b`
