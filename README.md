# vlm-repo
VLMを試すリポジトリ

## 概要
このリポジトリは、Vision Language Model (VLM) を試すための環境です。
以下の方法でVLMを使用できます：

1. **Transformers ライブラリを使用** (`vlm_transformers.py`)
   - HuggingFaceのモデルを直接使用
   - ローカルで動作（初回実行時にモデルをダウンロード）
   - インターネット接続不要（モデルダウンロード後）

2. **API を使用** (`vlm_api.py`)
   - OpenAI GPT-4 Vision APIを使用
   - APIキーが必要
   - 常にインターネット接続が必要

3. **R-4B モデルを使用** (`R-4B/vlm_r4b.py`)
   - YannQi/R-4B 専用スクリプト
   - HuggingFaceのR-4Bモデルを使用
   - 詳細は `R-4B/README.md` を参照

## セットアップ

### 1. uv のインストール
```bash
# uvをインストール（まだの場合）
pip install uv
```

### 2. 依存関係のインストール
```bash
# プロジェクトのディレクトリに移動
cd vlm-repo

# uvを使って依存関係をインストール
uv sync
```

## 使い方

### Transformers を使用する場合

```bash
# uvの仮想環境でスクリプトを実行
uv run python vlm_transformers.py <画像パス> "<質問>"

# 例：
uv run python vlm_transformers.py sample.jpg "この画像には何が写っていますか？"
```

**注意:** 
- 初回実行時に大きなモデル（数GB）がダウンロードされます
- GPUが利用可能な場合は自動的に使用されます
- メモリ使用量が大きいため、十分なRAMが必要です

### API を使用する場合

```bash
# OpenAI APIキーを環境変数に設定
export OPENAI_API_KEY="your-api-key-here"

# スクリプトを実行
uv run python vlm_api.py <画像パス> "<質問>"

# 例：
uv run python vlm_api.py sample.jpg "この画像には何が写っていますか？"
```

**注意:**
- OpenAI APIキーが必要です
- API使用料金が発生します
- インターネット接続が必要です

### R-4B モデルを使用する場合

```bash
# R-4Bモデルでスクリプトを実行
uv run python R-4B/vlm_r4b.py <画像パス> "<質問>"

# 例：
uv run python R-4B/vlm_r4b.py sample.jpg "この画像には何が写っていますか？"
```

**注意:**
- R-4Bモデルがダウンロードされます（数GB）
- 詳細な使用方法は `R-4B/README.md` を参照してください

## ファイル構成

```
vlm-repo/
├── .gitignore           # Git除外設定
├── .python-version      # Python バージョン指定
├── pyproject.toml       # プロジェクト設定と依存関係
├── README.md            # このファイル
├── vlm_transformers.py  # Transformersを使用したVLM実装
├── vlm_api.py          # APIを使用したVLM実装
└── R-4B/               # R-4Bモデル専用ディレクトリ
    ├── README.md        # R-4Bの使用方法
    ├── example.md       # 使用例
    └── vlm_r4b.py      # R-4Bモデル実行スクリプト
```

## 依存関係

- Python >= 3.12.3
- transformers >= 4.40.0
- torch >= 2.0.0
- pillow >= 10.0.0
- openai >= 1.0.0
- requests >= 2.31.0

## トラブルシューティング

### モデルのダウンロードが遅い場合
初回実行時はモデルのダウンロードに時間がかかります。気長にお待ちください。

### メモリ不足エラー
Transformers版を使用する場合、十分なメモリ（RAM）が必要です。
メモリが不足する場合は、API版の使用を検討してください。

### APIキーエラー
API版を使用する場合は、必ず環境変数 `OPENAI_API_KEY` を設定してください。

## ライセンス
MIT License
