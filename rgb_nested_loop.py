#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: April 26, 2025
# This program displays all the Rgb color in a 15 increment


def main():

    # Nested Loop for all colors
    for r in range(0, 256, 15):
        for g in range(0, 256, 15):
            for b in range(0, 256, 15):

                # Print colors!
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m ".format(
                        r, g, b, (("RGB"), r, g, b)
                    )
                )


if __name__ == "__main__":
    main()
