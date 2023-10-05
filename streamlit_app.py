import streamlit as st
import time
import math

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def main():
    st.title("素因数分解時間計測アプリ")
    st.write("このアプリは、与えられた整数の素因数分解を行い、所要時間を計測します.")
    number_to_factorize = st.number_input("素因数分解対象の数を入力してください:", min_value=1)

    if st.button("1回計測"):
        start_time = time.time()
        factors = factorize(number_to_factorize)
        end_time = time.time()
        elapsed_time = end_time - start_time
        st.write(f"素因数分解結果: {factors}")
        st.write(f"素因数分解にかかる時間: {elapsed_time:.4f} 秒")

    if st.button("100回計測"):  # 100回計測ボタンを追加
        elapsed_times = []
        for i in range(100):  # 100回計算
            start_time = time.time()
            factors = factorize(number_to_factorize)
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_times.append(elapsed_time)
        avg_elapsed_time = sum(elapsed_times) / len(elapsed_times)
        st.write(f"100回素因数分解の平均時間: {avg_elapsed_time:.4f} 秒")

if __name__ == "__main__":
    main()


 

