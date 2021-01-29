#!/bin/bash
if [ -d "$HOME/.config/i3/" ]; then
	echo "Installing i3 configuration..."
	cp -rp * $HOME/.config/i3/
	echo "Done."
else
	echo "Creating directory for i3..."
	mkdir $HOME/.config/i3
	echo "Installing i3 configuration..."
	cp -rp * $HOME/.config/i3/
	echo "Done"
fi
