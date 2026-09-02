# A Different Kind of Hello

A tiny, minimalist, interactive "hello" — built with Streamlit.

It progressively reveals a short sequence: an opening hello, a sketch reveal,
one small interactive question, and a quiet closing line. No autoplay audio,
no clutter, and it degrades gracefully if the sketch or song files are missing.

---

## 1. Project structure

```
stella/
├── app.py
├── requirements.txt
├── README.md
└── assets/
    ├── sketch.jpg   (add this yourself)
    └── song.mp3     (optional — add this yourself)
```

## 2. Install Streamlit

Make sure you have Python 3.9+ installed, then from inside the `stella/`
folder run:

```bash
pip install -r requirements.txt
```

This installs Streamlit (and nothing else — the app has no other dependencies).

## 3. Add your files

- Put your sketch image at `assets/sketch.jpg` (JPG or PNG both work — if you
  use a PNG, just make sure the filename inside `assets/` matches what
  `app.py` expects, or rename your file to `sketch.jpg`).
- Optionally, put a short song at `assets/song.mp3`.
- If either file is missing, the page still works — it just skips that
  piece gracefully (no image placeholder box, no music button).

## 4. Run it locally

From inside the `stella/` folder:

```bash
streamlit run app.py
```

Streamlit will open a local browser tab (usually `http://localhost:8501`).
Open it on your phone (same Wi-Fi network) using the "Network URL" Streamlit
prints in the terminal, to preview the mobile experience.

## 5. Upload the project to GitHub

1. Create a new **public** or **private** repository on GitHub (e.g. `stella`).
2. From inside the `stella/` folder, run:

```bash
git init
git add .
git commit -m "A Different Kind of Hello"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

> If your sketch or song files are large or you'd rather not have them in a
> public repo's history, you can add `assets/sketch.jpg` and `assets/song.mp3`
> to a `.gitignore` and upload them directly through Streamlit Community
> Cloud's file manager after deployment instead.

## 6. Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with
   GitHub.
2. Click **"New app"**.
3. Select your repository, branch (`main`), and set the main file path to
   `app.py`.
4. Click **Deploy**.
5. Once it's live, you'll get a shareable link like:
   `https://<your-app-name>.streamlit.app`

That's it — that link is what you'd send instead of a normal "hello."

---

### Notes

- No autoplay: the music only starts after the visitor's first tap, in line
  with what browsers allow anyway.
- Everything is intentionally quiet — no hearts, no confetti, no romantic
  language. If you want to change any of the copy, it all lives as plain
  strings inside `app.py`, clearly separated by screen (`screen_hello`,
  `screen_reveal`, `screen_question`, `screen_answered`).
