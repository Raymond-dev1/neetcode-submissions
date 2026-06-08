class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if(s.length !== t.length) return false;

        const count : Record< string ,number > ={};
        for (const char of s){
            count[char] =(count[char] || 0 ) +1
        }
        for (const char of t){
            count[char] =(count[char] || 0) -1
        }
        return Object.values(count).every(v => v=== 0)
    }
}
