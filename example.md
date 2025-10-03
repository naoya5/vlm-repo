# 使用例 (Examples)

## 準備
まず、画像ファイルを用意します。例えば `sample.jpg` という名前で保存します。

## Transformers を使用した例

### 基本的な使い方
```bash
# 画像の内容を質問
uv run python vlm_transformers.py sample.jpg "この画像には何が写っていますか？"

# 画像の詳細を質問
uv run python vlm_transformers.py sample.jpg "この画像に写っている物体を詳しく説明してください。"

# 特定の要素について質問
uv run python vlm_transformers.py photo.jpg "この写真に人は何人写っていますか？"
```

### 注意点
- 初回実行時は数GBのモデルがダウンロードされるため、時間がかかります
- GPUがある場合は自動的に使用され、高速に処理されます
- メモリが不足する場合は、API版の使用をおすすめします

## API を使用した例

### 環境変数の設定
```bash
# OpenAI APIキーを設定（1回のみ）
export OPENAI_API_KEY="sk-your-api-key-here"
```

### 基本的な使い方
```bash
# 画像の内容を質問
uv run python vlm_api.py sample.jpg "この画像には何が写っていますか？"

# 英語で質問
uv run python vlm_api.py photo.jpg "What do you see in this image?"

# 詳細な分析を依頼
uv run python vlm_api.py artwork.jpg "この作品の芸術的な特徴を分析してください。"
```

### 注意点
- OpenAI APIキーが必要です（https://platform.openai.com/api-keys で取得）
- API使用料金が発生します
- インターネット接続が必要です

## よくある質問

### Q: どちらの方法を使えばいいですか？
A: 
- **Transformers版**: オフラインで使いたい、APIコストを気にする場合
- **API版**: 簡単に始めたい、高品質な結果が欲しい場合

### Q: サポートされている画像形式は？
A: 
- JPEG (.jpg, .jpeg)
- PNG (.png)
- その他のPillow/PIL対応形式

### Q: 日本語で質問できますか？
A: はい、両方とも日本語の質問に対応しています。

### Q: エラーが出た場合は？
A: README.mdのトラブルシューティングセクションを参照してください。
