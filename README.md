# GhatGPT CasaOS AppStore

Рабочий репозиторий CasaOS AppStore для установки локального AI-сервера:

- `GhatGPT Stack` — GhatGPT + Ollama GPU.
- `Ollama GPU` — отдельный сервер Ollama с NVIDIA GPU.
- `GhatGPT` — панель на порту `3000`.
- `Server Monitor 3420` — панель мониторинга на порту `3420`.
- `Install All Models` — установка всех моделей.
- Отдельные установщики моделей в `Apps/model-*`.

## URL для CasaOS

Добавлять в CasaOS как Custom App Store:

```text
https://github.com/Sert1985n/GhatGPT
```

Если CasaOS просит ZIP:

```text
https://github.com/Sert1985n/GhatGPT/archive/refs/heads/main.zip
```

## Порты

- GhatGPT: `3000`
- Ollama API: `11434`
- Monitor: `3420`

## Важно

- Модели хранятся в `/opt/ollama`.
- Эту папку не удалять.
- Модельные приложения требуют, чтобы сначала был запущен `Ollama GPU` или `GhatGPT Stack`.
- Все модели создают русские alias `ru-*`.
