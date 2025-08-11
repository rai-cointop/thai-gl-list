#!/bin/bash

# Vue をビルド
cd frontend
npm install
npm run build

# ビルド結果を Flask の static にコピー
rm -rf ../backend/static
mkdir -p ../backend/static
cp -r dist/* ../backend/static/
