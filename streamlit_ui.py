# app.py

import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="CRUD Operations", page_icon="📁")

st.title("📁 CRUD Operations Project")

# ---------------- FILE OPERATIONS ---------------- #

def create_file(file_name, content):
    p = Path(file_name)

    if p.exists():
        return "FILE ALREADY EXISTS!"

    with open(file_name, 'w') as file:
        file.write(content)

    return "FILE CREATED SUCCESSFULLY!"


def read_file(file_name):
    p = Path(file_name)

    if p.exists():
        with open(file_name, 'r') as file:
            return file.read()

    return "FILE NOT FOUND!"


def update_file(file_name, content, mode):
    p = Path(file_name)

    if p.exists():

        if mode == "Overwrite":
            with open(file_name, 'w') as file:
                file.write(content)

        elif mode == "Append":
            with open(file_name, 'a') as file:
                file.write(content)

        return "FILE UPDATED SUCCESSFULLY!"

    return "FILE DOES NOT EXIST!"


def delete_file(file_name):
    p = Path(file_name)

    if p.exists():
        os.remove(p)
        return "FILE DELETED SUCCESSFULLY!"

    return "FILE DOES NOT EXIST!"


def rename_file(old_name, new_name):
    p = Path(old_name)

    if p.exists():
        p.rename(new_name)
        return "FILE RENAMED SUCCESSFULLY!"

    return "FILE NOT FOUND!"


# ---------------- FOLDER OPERATIONS ---------------- #

def create_folder(folder_name):
    p = Path(folder_name)

    if p.exists():
        return "FOLDER ALREADY EXISTS!"

    p.mkdir()
    return "FOLDER CREATED SUCCESSFULLY!"


def delete_folder(folder_name):
    p = Path(folder_name)

    if p.exists():
        p.rmdir()
        return "FOLDER DELETED SUCCESSFULLY!"

    return "FOLDER NOT FOUND!"


# ---------------- SIDEBAR ---------------- #

operation = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)

# ---------------- UI ---------------- #

if operation == "Create File":
    st.subheader("Create File")

    file_name = st.text_input("Enter File Name")
    content = st.text_area("Enter File Content")

    if st.button("Create"):
        result = create_file(file_name, content)
        st.success(result)


elif operation == "Read File":
    st.subheader("Read File")

    file_name = st.text_input("Enter File Name")

    if st.button("Read"):
        result = read_file(file_name)
        st.text(result)


elif operation == "Update File":
    st.subheader("Update File")

    file_name = st.text_input("Enter File Name")

    mode = st.radio(
        "Choose Update Type",
        ["Overwrite", "Append"]
    )

    content = st.text_area("Enter New Content")

    if st.button("Update"):
        result = update_file(file_name, content, mode)
        st.success(result)


elif operation == "Delete File":
    st.subheader("Delete File")

    file_name = st.text_input("Enter File Name")

    if st.button("Delete"):
        result = delete_file(file_name)
        st.success(result)


elif operation == "Rename File":
    st.subheader("Rename File")

    old_name = st.text_input("Enter Old File Name")
    new_name = st.text_input("Enter New File Name")

    if st.button("Rename"):
        result = rename_file(old_name, new_name)
        st.success(result)


elif operation == "Create Folder":
    st.subheader("Create Folder")

    folder_name = st.text_input("Enter Folder Name")

    if st.button("Create Folder"):
        result = create_folder(folder_name)
        st.success(result)


elif operation == "Delete Folder":
    st.subheader("Delete Folder")

    folder_name = st.text_input("Enter Folder Name")

    if st.button("Delete Folder"):
        result = delete_folder(folder_name)
        st.success(result)
        