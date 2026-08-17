# Deploying this folder as a Hugging Face Space

These files are developed in the `free-ai-notebooks` GitHub repo, but a
Hugging Face Space is its **own** git repository — you push this folder's
contents to it separately. Follow these steps once.

## 1. Create the Space

1. Go to <https://huggingface.co/new-space>.
2. **Owner:** your account or org (e.g. `thebuildai`).
3. **Space name:** `ardy-motion-generator` (SEO-friendly, matches the model
   name — people searching "ardy huggingface" or "nvidia ardy demo" will
   find it).
4. **License:** `apache-2.0`.
5. **Space SDK:** `Gradio`.
6. **Hardware:**
   - Choose **ZeroGPU** if it's available for your account (requires HF PRO
     or a community GPU grant) — this keeps the Space free to run.
   - Otherwise choose a small paid persistent GPU tier (e.g. `T4 small`).
     The code degrades gracefully: `@spaces.GPU` becomes a no-op on
     non-ZeroGPU hardware.
7. Click **Create Space**.

## 2. Push these files to the Space

Clone the new (empty) Space repo somewhere **outside** this project, copy
the contents of this folder into it, then push:

```bash
git clone https://huggingface.co/spaces/<owner>/ardy-motion-generator
cd ardy-motion-generator

# Copy every file from free-ai-notebooks/spaces/ardy-motion-generator/
# (README.md, app.py, requirements.txt, packages.txt, .gitignore) into
# this folder, then:

git add .
git commit -m "Initial ARDY Motion Generator Space"
git push
```

## 3. Add the Hugging Face token secret

The Space needs a token with **approved access** to
[`meta-llama/Meta-Llama-3-8B-Instruct`](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct):

1. Request access on the model page and wait for approval.
2. Create a read token at <https://huggingface.co/settings/tokens>.
3. In the Space: **Settings → Repository secrets → New secret**
   - Name: `HF_TOKEN`
   - Value: your token

## 4. Wait for the first build

The first build clones `nv-tlabs/ardy` and compiles its C++ extension
(`cmake`/`build-essential`, already declared in `packages.txt`). The first
**generation request** afterward downloads Llama-3-8B (~16 GB) and the ARDY
checkpoint, which can take several minutes. Subsequent requests reuse the
already-downloaded weights as long as the Space container stays warm.

## 5. Share the link back

Once it's live, send the Space URL
(`https://huggingface.co/spaces/<owner>/ardy-motion-generator`) so it can be
added to the `README.md` Notebooks table in `free-ai-notebooks`.

## Troubleshooting

- **"No module named 'ardy'" errors:** the first-run `pip install -e .` step
  in `app.py` failed — check the Space's build/runtime logs; usually a
  missing `cmake`/`build-essential` (verify `packages.txt` was picked up).
- **Subprocess doesn't see the GPU on ZeroGPU hardware:** `@spaces.GPU`
  forwards CUDA visibility through the process environment, and
  `subprocess.run` in `app.py` is called with `env=os.environ.copy()`, so it
  should inherit it. If generation silently falls back to CPU (very slow),
  open an issue — the fix is to call ARDY's Python API in-process instead of
  shelling out to `scripts/generate.py`.
- **401/403 downloading Llama-3-8B:** the `HF_TOKEN` secret's account either
  hasn't been granted access yet or the token lacks read permission.
