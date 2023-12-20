import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Suppress the warning

    st.title('Advanced Data Visualizer App')

    # Dataset selection
    datasets = {
        "Iris Dataset": sns.load_dataset('iris'),
        "Tips Dataset": sns.load_dataset('tips'),
        "Titanic Dataset": sns.load_dataset('titanic')
    }

    selected_dataset_name = st.selectbox("Select a dataset", list(datasets.keys()))

    selected_dataset = datasets[selected_dataset_name]

    # Display the selected dataset
    st.write("### Selected Dataset:")
    st.write(selected_dataset.head())

    st.markdown("---")

    # Visualization section
    st.subheader("Data Visualization")

    # Plot types selection
    plot_types = ["Histogram", "Pairplot", "Count Plot"]

    selected_plot = st.selectbox("Select a plot type", plot_types)

    if selected_plot == "Histogram":
        st.write("### Histogram")
        selected_column = st.selectbox("Select a column for Histogram", selected_dataset.columns)
        hist_kws = dict(alpha=0.7)
        fig, ax = plt.subplots()
        sns.histplot(data=selected_dataset, x=selected_column, kde=True, color="skyblue", **hist_kws)
        st.pyplot(fig)

    elif selected_plot == "Pairplot":
        st.write("### Pairplot")
        palette = sns.color_palette("husl")
        fig = sns.pairplot(selected_dataset, palette=palette)
        st.pyplot(fig.fig)

    elif selected_plot == "Count Plot":
        st.write("### Count Plot")
        selected_column = st.selectbox("Select a column for Count Plot", selected_dataset.columns)
        fig, ax = plt.subplots()
        sns.countplot(data=selected_dataset, x=selected_column, palette="Set2")
        st.pyplot(fig)

    # Additional options or descriptions can be added here

if __name__ == '__main__':
    main()
