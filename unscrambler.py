#!/usr/bin/python3

import string
import argparse
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX'
print(alphabet)

def get_map(new_alphabet):
	return [alphabet.index(letter) for letter in new_alphabet]

def get_mapped_letters(string, new_alphabet):
	result = [*string]
	alphabet_map = get_map(new_alphabet)
	for i, char in enumerate(string):
		result[alphabet_map[i]] = char
	return ''.join(result)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Unscrambler for OliCyber 2024 challenge")
	parser.add_argument('new_alphabet', type=str, help="the result of encrypt(alphabet)")
	parser.add_argument('--string', type=str, help="string to unscramble")

	args = parser.parse_args()

	print("new alphabet", args.new_alphabet)
	print("map", get_map(args.new_alphabet))
	if args.string:
		print("result", get_mapped_letters(args.string, args.new_alphabet))