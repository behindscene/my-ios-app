# Appetize.io Integration Setup Guide

View your WholesaleConnect iOS app in a browser on Windows - no Mac needed.

---

## How it works

Every time you push code to GitHub, a macOS build runner automatically:
1. Compiles your Swift app for the iOS Simulator
2. Uploads it to Appetize.io
3. Posts a preview link in the GitHub Actions summary

---

## One-time setup (10 minutes)

### Step 1 - Get your Appetize API token

1. Go to https://appetize.io and create a free account
2. Navigate to Account -> API
3. Copy your API Token

Free plan includes 100 minutes/month of streaming - plenty for testing.

---

### Step 2 - Add secrets to your GitHub repo

1. Go to your GitHub repo -> Settings -> Secrets and variables -> Actions
2. Click New repository secret and add APPETIZE_API_TOKEN and APPETIZE_PUBLIC_KEY

---

### Step 3 - Watch the build

1. Go to your GitHub repo -> Actions tab
2. You will see the Build & Deploy to Appetize.io workflow running
3. When it finishes (10-15 min), click the run -> scroll to Summary
4. You will see a link: Open in Appetize.io

---

### Step 4 - Save the Public Key

After the first build, copy the Appetize Public Key from the job summary and save it as the APPETIZE_PUBLIC_KEY secret. This ensures future pushes update the same app.

---

## Viewing your app on Windows

1. Open the Appetize link in any browser on Windows
2. Click Tap to play
3. Your iOS app runs in a virtual iPhone - no Mac, no Xcode!

---

## Triggering a build manually

1. GitHub repo -> Actions -> Build & Deploy to Appetize.io
2. Click Run workflow

---

## Troubleshooting

- Build fails No scheme found: Make sure project.yml is committed and pushed
- Build fails Xcode not found: The runner auto-selects Xcode 16 on macos-15
- Appetize upload fails: Double-check APPETIZE_API_TOKEN secret is set correctly
- App shows blank screen: Update AppConfig.swift to point to your deployed API URL

---

## Pointing the app at your backend

When running in Appetize, the app runs on Appetize servers and cannot reach localhost.
Update App/AppConfig.swift to use your deployed API URL.
