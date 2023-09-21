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

 

    number_to_factorize = st.number_input("素因数分解対象の数を入力してください:", min_value=1, value=1234567890)

 

    if st.button("計測開始"):
        start_time = time.time()

 

        factors = factorize(number_to_factorize)

 

        end_time = time.time()
        elapsed_time = end_time - start_time

 

        st.write(f"素因数分解結果: {factors}")
        st.write(f"素因数分解にかかる時間: {elapsed_time:.4f} 秒")

 

if __name__ == "__main__":
    main()