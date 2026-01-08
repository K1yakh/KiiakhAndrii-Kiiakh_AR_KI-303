import Solution

if __name__ == "__main__":
    txtFile = "result.txt"
    binFile = "result.bin"
    
    Solution.solution(txtFile, binFile)
    
    print(f"Content of file {txtFile} is:\n{Solution.read_txt(txtFile)}")
    
    Solution.read_binary(binFile)