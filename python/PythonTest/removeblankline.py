def delblankline(infile, outfile):
	infp = open(infile, "r")
	outfp = open(outfile, "w")
	lines = infp.readlines()
	for li in lines:
		if li!='':
			outfp.writelines(li)
	infp.close()
	outfp.close()

if __name__ == "__main__":
	delblankline("rslist2.txt","rslist3.txt")
