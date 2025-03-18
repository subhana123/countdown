import streamlit as st
import time

def main():
    st.set_page_config(page_title="Countdown Timer", page_icon="⏳")
    st.title("⏳ Countdown Timer")

    # Timer input
    minutes = st.number_input("Enter minutes:", min_value=0, max_value=60, value=0)
    seconds = st.number_input("Enter seconds:", min_value=0, max_value=59, value=0)

    if st.button("Start Timer"):
        total_seconds = int(minutes * 60 + seconds)

        if total_seconds > 0:
            st.write("Timer started!")

            with st.empty():
                while total_seconds > 0:
                    mins, secs = divmod(total_seconds, 60)
                    timer_text = f"{mins:02d}:{secs:02d}"
                    st.markdown(f"## ⏰ Time Remaining: {timer_text}")
                    time.sleep(1)
                    total_seconds -= 1

            st.success("⏳ Time's up!")
        else:
            st.warning("Please set a valid time.")


if __name__ == "__main__":
    main()
