use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn sanitize_12306_name(name: &str) -> String {
    // 12306 System Logic: 
    // 1. Force Uppercase
    // 2. Remove all non-alphabetic characters (including spaces and symbols)
    // 3. This matches the 'single string' matching logic of the HSR backend
    
    name.chars()
        .filter(|c| c.is_alphabetic())
        .collect::<String>()
        .to_uppercase()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sanitization() {
        assert_eq!(sanitize_12306_name("John Doe"), "JOHNDOE");
        assert_eq!(sanitize_12306_name("O'Connor"), "OCONNOR");
        assert_eq!(sanitize_12306_name("Smith-Jones"), "SMITHJONES");
    }
}
