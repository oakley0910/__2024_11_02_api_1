import streamlit as st

st.write('## 第3章')
st.write('## 第4節')
st.write('___')
st.write('Hello! **streamlit**')


import random

def generate_lotto_numbers():
    # 生成 1 到 49 的號碼，並隨機選擇 6 個不重複的號碼
    lotto_numbers = random.sample(range(1, 50), 6)
    
    # 隨機選擇一個特別號
    special_number = random.choice(lotto_numbers)
    
    # 返回號碼和特別號
    return sorted(lotto_numbers), special_number

def main():
    # 生成大樂透號碼
    lotto_numbers, special_number = generate_lotto_numbers()
    
    # 輸出結果
    print("本期大樂透電腦選號號碼如下:")
    print(" ".join(map(str, lotto_numbers)))  # 顯示排序後的號碼
    print(f"特別號:{special_number}")

if __name__ == "__main__":
    main()