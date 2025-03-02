from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class NutrientInfo(BaseModel):
    amount: Optional[float] = Field(None, description="The amount of the nutrient")
    unit: Optional[str] = Field(None, description="The unit of measurement (g, mg, mcg, etc.)")
    daily_value_percent: Optional[float] = Field(None, description="The percentage of daily value")


class NutritionFactsLabel(BaseModel):
    serving_size: Optional[str] = Field(None, description="The serving size, typically represented as a quantity with unit")
    servings_per_container: Optional[float] = Field(None, description="Number of servings per container")
    calories: Optional[int] = Field(None, description="Total calories per serving")
    
    total_fat: Optional[NutrientInfo] = Field(None, description="Total fat content per serving")
    saturated_fat: Optional[NutrientInfo] = Field(None, description="Saturated fat content per serving")
    trans_fat: Optional[NutrientInfo] = Field(None, description="Trans fat content per serving")
    polyunsaturated_fat: Optional[NutrientInfo] = Field(None, description="Polyunsaturated fat content per serving")
    monounsaturated_fat: Optional[NutrientInfo] = Field(None, description="Monounsaturated fat content per serving")
    
    cholesterol: Optional[NutrientInfo] = Field(None, description="Cholesterol content per serving")
    sodium: Optional[NutrientInfo] = Field(None, description="Sodium content per serving")
    
    total_carbohydrate: Optional[NutrientInfo] = Field(None, description="Total carbohydrate content per serving")
    dietary_fiber: Optional[NutrientInfo] = Field(None, description="Dietary fiber content per serving")
    total_sugars: Optional[NutrientInfo] = Field(None, description="Total sugars content per serving")
    added_sugars: Optional[NutrientInfo] = Field(None, description="Added sugars content per serving")
    sugar_alcohols: Optional[NutrientInfo] = Field(None, description="Sugar alcohols content per serving")
    
    protein: Optional[NutrientInfo] = Field(None, description="Protein content per serving")
    
    # Vitamins and minerals
    vitamin_d: Optional[NutrientInfo] = Field(None, description="Vitamin D content per serving")
    calcium: Optional[NutrientInfo] = Field(None, description="Calcium content per serving")
    iron: Optional[NutrientInfo] = Field(None, description="Iron content per serving")
    potassium: Optional[NutrientInfo] = Field(None, description="Potassium content per serving")
    vitamin_a: Optional[NutrientInfo] = Field(None, description="Vitamin A content per serving")
    vitamin_c: Optional[NutrientInfo] = Field(None, description="Vitamin C content per serving")
    
    # Additional nutrients that might be present
    additional_nutrients: Optional[Dict[str, NutrientInfo]] = Field(None, description="Additional nutrients not covered by standard fields")
    
    # Additional information
    ingredients: Optional[str] = Field(None, description="List of ingredients")
    allergens: Optional[List[str]] = Field(None, description="List of allergens")
    manufacturer: Optional[str] = Field(None, description="Manufacturer or distributor of the product")
    product_name: Optional[str] = Field(None, description="Name of the product")
