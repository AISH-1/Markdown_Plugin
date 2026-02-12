#!/bin/bash
WORKSPACE_ROOT=$(pwd)
PLUGIN_NAME=$(basename "$WORKSPACE_ROOT")

cd "$WORKSPACE_ROOT/.."

rm -rf "$PLUGIN_NAME.difypkg"

dify plugin package "$PLUGIN_NAME"
