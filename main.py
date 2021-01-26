import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

## タイトルの表示
st.title("Streamlit 超入門")

## テキストの表示
st.write("DataFrame")

## データフレームの表示
df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [10, 20, 30, 40]
})
st.write(df.style.highlight_max(axis=0))
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
st.table(df.style.highlight_max(axis=0))

## マークダウンの表示

"""
# 1章
## 1.1節
### 1.1.1項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

## チャートの表示
df_chart = pd.DataFrame(
    np.random.rand(20, 3),
    columns = {"a", "b", "c"}
)

st.line_chart(df_chart)
st.area_chart(df_chart)
st.bar_chart(df_chart)
# st.pyplot(df_chart)

## 地図の表示
df_map = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns = {"lat", "lon"}
)

st.map(df_map)

## 画像の表示
img = Image.open("test.jpg")
st.image(img, caption="Test Image", use_column_width=True)


## チェックボックスの表示
if st.checkbox("Show Hello") == True:
    st.write("Hello")

## セレクトボックスの表示
option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1, 10))
)

"あなたの好きな数字は、", option, "です。"

## テキストボックスの表示
text = st.text_input("あなたの趣味を教えてください。")
"あなたの趣味：", text

## スライダの表示
condition = st.slider("あなたの今の調子は？", 0, 100, 50)
"コンディション：", condition

## サイドバーの追加
st.sidebar.write("サイドバーです")
text2 = st.sidebar.text_input("あなたの趣味を教えてください。２")
condition2 = st.sidebar.slider("あなたの今の調子は？２", 0, 100, 50)

"あなたの趣味：", text2
"コンディション：", condition2


## 2カラムレイアウト
left_column, right_column = st.beta_columns(2)

button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

## エクスパンダー
"エクスパンダーの表示"
expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ1回答")
expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ2回答")
expander3 = st.beta_expander("問い合わせ3")
expander3.write("問い合わせ3回答")


## プログレスバーの表示
st.write("プログレスバーの表示")
"Start!!"
latest_iteration = st.empty()
bar = st.progress(0) # 0: 0-100, 0.0: 0.0-1.0

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
"Done"
