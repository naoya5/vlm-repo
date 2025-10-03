# R-4B Vision Language Model

このディレクトリには、YannQi/R-4B モデルを使用するためのスクリプトが含まれています。

## モデルについて

R-4B は HuggingFace でホストされている Vision Language Model です。
モデルの詳細: https://huggingface.co/YannQi/R-4B

## セットアップ

### 1. 依存関係のインストール

プロジェクトのルートディレクトリで以下を実行：

```bash
cd ..
uv sync
```

## 使い方

### 基本的な使い方

```bash
# プロジェクトルートからの実行
uv run python R-4B/vlm_r4b.py <画像パス> "<質問>"

# または R-4B ディレクトリ内からの実行
cd R-4B
uv run python vlm_r4b.py <画像パス> "<質問>"
```

### 使用例

```bash
# 日本語で質問
uv run python R-4B/vlm_r4b.py sample.jpg "この画像には何が写っていますか？"

# 英語で質問
uv run python R-4B/vlm_r4b.py photo.jpg "What do you see in this image?"

# 詳細な説明を求める
uv run python R-4B/vlm_r4b.py artwork.jpg "この画像に写っている物体を詳しく説明してください。"

# 特定の要素について質問
uv run python R-4B/vlm_r4b.py scene.jpg "この写真に人は何人写っていますか？"
```

## 注意事項

- **初回実行時**: 数GBのモデルがダウンロードされるため、時間がかかります
- **GPU推奨**: GPUが利用可能な場合は自動的に使用され、高速に処理されます
- **メモリ要件**: 十分なRAMが必要です（最低8GB推奨）
- **インターネット接続**: 初回のモデルダウンロード時に必要です

## トラブルシューティング

### モデルのダウンロードが遅い場合
初回実行時はモデルのダウンロードに時間がかかります。気長にお待ちください。

### メモリ不足エラー
十分なメモリ（RAM）が必要です。メモリが不足する場合は：
- 他のアプリケーションを閉じる
- より小さなモデルの使用を検討する
- APIベースのソリューション（vlm_api.py）を使用する

### モデルロードエラー
- インターネット接続を確認してください
- HuggingFace のアクセストークンが必要な場合があります
- `transformers` ライブラリが最新かどうか確認してください

## ファイル構成

```
R-4B/
├── README.md        # このファイル
└── vlm_r4b.py      # R-4Bモデル実行スクリプト
```

## サポートされている画像形式

- JPEG (.jpg, .jpeg)
- PNG (.png)
- その他のPillow/PIL対応形式

## 日本語・英語対応

このモデルは日本語と英語の両方の質問に対応しています。
質問は自然言語で自由に入力できます。
