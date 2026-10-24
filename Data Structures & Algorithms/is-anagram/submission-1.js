class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false
  
        const aCode = 'a'.charCodeAt(0)
        let count = new Array(26).fill(0)
        
        for (let i = 0; i < s.length; i++) {
            count[s.charCodeAt(i) - aCode]++
            count[t.charCodeAt(i) - aCode]--
        }
        
        return count.every((val) => val === 0);
    }
}
