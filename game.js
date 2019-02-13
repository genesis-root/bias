function case_generator(){
    var declensions = ["accusative singular", "accusative singular", "genitive singular", "dative singular", "ablative singular", "vocative singular"];

    return declensions[Math.floor(Math.random() * 4) + 1]
}

function case_ending_first_fem(){
    case_type = case_generator();
    if (case_type == "accusative singular") {
        return "accusative"
    }
    if (case_type == "dative singular") {
        return "dative"
    }
    if (case_type == "ablative singular") {
        return "ablative"
    }
    if (case_type == "vocative singular") {
        return "vocative"
    }
}

function decline(noun) {
    case_type = case_generator();
    declension = case_ending_first_fem(case_type);
    if (noun.slice(noun.length-1) == "a") {
        return noun.slice(0, noun.length - 1) + declension
    }
    if (noun.slice(noun.length - 2, noun.length) == "us") {
        return noun.slice(0, noun.length - 2) + declension
    }
    if (noun.slice(noun.length - 2, noun.length) == "um") {
        return noun.slice(0, noun.length - 2) + declension
    }
}

x = case_ending_first_fem()
console.log(x);