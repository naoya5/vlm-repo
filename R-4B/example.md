# R-4B 使用例 (Examples)

## 準備

まず、画像ファイルを用意します。例えば `sample.jpg` という名前で保存します。

## 基本的な使い方

### プロジェクトルートから実行

```bash
# 日本語で質問
uv run python R-4B/vlm_r4b.py sample.jpg "この画像には何が写っていますか？"

# 英語で質問
uv run python R-4B/vlm_r4b.py sample.jpg "What is in this image?"

# 画像の詳細を質問
uv run python R-4B/vlm_r4b.py sample.jpg "この画像に写っている物体を詳しく説明してください。"

# 特定の要素について質問
uv run python R-4B/vlm_r4b.py photo.jpg "この写真に人は何人写っていますか？"
```

### R-4B ディレクトリから実行

```bash
cd R-4B

# 基本的な使い方
uv run python vlm_r4b.py ../sample.jpg "この画像には何が写っていますか？"

# 複数の質問を試す
uv run python vlm_r4b.py ../photo1.jpg "この画像の主な色は何ですか？"
uv run python vlm_r4b.py ../photo2.jpg "この画像の雰囲気を説明してください。"
```

## 実行例

### 例1: 一般的な画像認識

```bash
uv run python R-4B/vlm_r4b.py cat.jpg "この画像には何が写っていますか？"
```

**期待される出力:**
```
=== R-4B Vision Language Model ===

Loading model: YannQi/R-4B...
Model loaded successfully!

Image: cat.jpg
Question: この画像には何が写っていますか？

Generating response...
Answer:
この画像には猫が写っています。...
```

### 例2: 詳細な説明を求める

```bash
uv run python R-4B/vlm_r4b.py landscape.jpg "この風景の特徴を詳しく説明してください。"
```

### 例3: 特定の要素をカウント

```bash
uv run python R-4B/vlm_r4b.py group_photo.jpg "この写真に何人写っていますか？"
```

### 例4: 英語での質問

```bash
uv run python R-4B/vlm_r4b.py artwork.jpg "Describe the artistic style of this image."
```

## よくある質問

### Q: どのような質問ができますか？
A: 
- 画像の内容を尋ねる一般的な質問
- 特定の物体や人物の数を数える
- 色、雰囲気、スタイルなどの特徴を説明する
- 画像内の関係性や配置について質問する

### Q: サポートされている画像形式は？
A: 
- JPEG (.jpg, .jpeg)
- PNG (.png)
- その他のPillow/PIL対応形式

### Q: 日本語と英語のどちらが良いですか？
A: 両方とも使用できます。モデルは多言語対応しており、質問の言語に応じて適切に回答します。

### Q: 初回実行時にエラーが出る場合は？
A: 
- インターネット接続を確認してください
- モデルのダウンロードには数GB必要です
- ダウンロードには時間がかかる場合があります

### Q: メモリが足りない場合は？
A: 
- 他のアプリケーションを閉じてください
- より小さなモデルの使用を検討してください
- API版（`vlm_api.py`）の使用を検討してください

## トラブルシューティング

### モデルのダウンロードが遅い
初回実行時は数GBのモデルをダウンロードするため、時間がかかります。
高速なインターネット接続を使用することをお勧めします。

### CUDA out of memory エラー
GPU メモリが不足している場合は、以下を試してください：
- より小さな画像を使用する
- `--no-cuda` オプションを使用してCPUで実行する（スクリプトの修正が必要）
- より小さなモデルを使用する

### Import エラー
必要な依存関係がインストールされていることを確認してください：
```bash
cd ..
uv sync
```

## 注意事項

- **モデルサイズ**: 数GBのディスク容量が必要です
- **実行時間**: 初回実行時はモデルのダウンロードに時間がかかります
- **GPU推奨**: GPUがある場合、処理が大幅に高速化されます
- **メモリ**: 十分なRAM（最低8GB推奨）が必要です
