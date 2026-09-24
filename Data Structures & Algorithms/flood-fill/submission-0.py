class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        
        if image[sr][sc] == color:
            return image

        self.fillElements(image, row, col, sr, sc, color, image[sr][sc])

        return image

    def fillElements(self, image: List[List[int]], r:int , c:int , sr:int , sc:int , color:int, base:int):
        if not (0 <= sr < r and 0 <= sc < c):
            return
        elif image[sr][sc] != base:
            return
        
        image[sr][sc] = color
        self.fillElements(image, r, c, sr + 1, sc, color, base)
        self.fillElements(image, r, c, sr - 1, sc, color, base)
        self.fillElements(image, r, c, sr, sc + 1, color, base)
        self.fillElements(image, r, c, sr, sc - 1, color, base)

        return
