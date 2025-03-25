class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        R = len(rectangles)
        
        sorted_y1 = sorted(r[1] for r in rectangles)
        sorted_y2 = sorted(r[3] for r in rectangles)

        cand_h = sorted({r[1] for r in rectangles} | {r[3] for r in rectangles})
        valid_h = []
        for h in cand_h:
            bottom = bisect_right(sorted_y2, h)
            top = R - bisect_left(sorted_y1, h)
            if bottom + top == R:
                valid_h.append(h)
        
        Lh = len(valid_h)
        i = 0
        j = 1
        found_horizontal = False
        while i < Lh - 1 and not found_horizontal:
            h1 = valid_h[i]
            bottom = bisect_right(sorted_y2, h1)
            if bottom == 0:
                i += 1
                continue
            j = i + 1
            while j < Lh and not found_horizontal:
                h2 = valid_h[j]
                top = R - bisect_left(sorted_y1, h2)
                if top == 0:
                    j += 1
                    continue
                if bisect_left(sorted_y1, h2) > bottom:
                    found_horizontal = True
                    break
                j += 1
            i += 1
        
        if found_horizontal:
            return True
        
        sorted_x1 = sorted(r[0] for r in rectangles)
        sorted_x2 = sorted(r[2] for r in rectangles)
        cand_v = sorted({r[0] for r in rectangles} | {r[2] for r in rectangles})
        valid_v = []
        for v in cand_v:
            left = bisect_right(sorted_x2, v)
            right = R - bisect_left(sorted_x1, v)
            if left + right == R:
                valid_v.append(v)
                
        Lv = len(valid_v)
        i = 0
        j = 1
        found_vertical = False
        while i < Lv - 1 and not found_vertical:
            v1 = valid_v[i]
            left = bisect_right(sorted_x2, v1)
            if left == 0:
                i += 1
                continue
            j = i + 1
            while j < Lv and not found_vertical:
                v2 = valid_v[j]
                right = R - bisect_left(sorted_x1, v2)
                if right == 0:
                    j += 1
                    continue
                if bisect_left(sorted_x1, v2) > left:
                    found_vertical = True
                    break
                j += 1
            i += 1
        
        return found_vertical
