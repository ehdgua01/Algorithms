fn bmi(weight: u32, height: f32) -> &'static str {
    let index = weight as f32 / height.powi(2);
    if index <= 18.5 {
        &"Underweight"
    } else if index <= 25.0 {
        &"Normal"
    } else if index <= 30.0 {
        &"Overweight"
    } else {
        &"Obese"
    }
}
