def checkmate(board):
    rows = board.split('\n')
    rows = [row for row in rows if row != ""]
    
    if not rows:
        return  
    size = len(rows)
    for row in rows:
        if len(row) != size:
            print("Error")
            return
    king_row = -1
    king_col = -1
    king_count = 0
    
    for r in range(size):
        for c in range(size):
            if rows[r][c] == 'K':
                king_row = r
                king_col = c
                king_count += 1
                
    if king_count != 1:
        print("Error")
        return
    def look_for_threat(dr, dc, dangerous_pieces, check_pawn=False):
        r = king_row + dr
        c = king_col + dc
        step = 1
        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
            
            if piece not in ['K', 'Q', 'R', 'B', 'P']:
                r += dr
                c += dc
                step += 1
                continue
                
            if piece in dangerous_pieces:
                return True
                
            if check_pawn and piece == 'P' and step == 1 and r == king_row + 1:
                return True
                
            return False
            
        return False

    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_directions:
        if look_for_threat(dr, dc, dangerous_pieces=['R', 'Q']):
            print("Success") # King is in check
            return
            
    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_directions:
        if look_for_threat(dr, dc, dangerous_pieces=['B', 'Q'], check_pawn=True):
            print("Success") # King is in check
            return
    print("Fail")