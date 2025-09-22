function solution(my_string, overwrite_string, s) {
    var answer = "";
    const str= [...my_string];
    str.splice(s, overwrite_string.length, overwrite_string);
    return str.join("");
}