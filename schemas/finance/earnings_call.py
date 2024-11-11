from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class FinancialMetric(BaseModel):
    metric_name: str = Field(
        ..., description="Name of the financial metric, e.g., 'Revenue', 'Net Income'."
    )
    value: float = Field(..., description="The value of the financial metric.")
    currency: Optional[str] = Field(
        None,
        description="Currency of the financial metric, if applicable, e.g., 'USD'.",
    )
    year_over_year_growth: Optional[float] = Field(
        None, description="Year-over-year growth percentage for the metric."
    )


class AnalystQuestion(BaseModel):
    analyst_name: str = Field(
        ..., description="Name of the analyst asking the question."
    )
    question_text: str = Field(
        ..., description="Text of the question asked by the analyst."
    )
    response_text: str = Field(
        ..., description="Response to the analyst's question from the company."
    )


class PerformanceSummary(BaseModel):
    summary_text: str = Field(
        ...,
        description="Summary of the company's performance as described in the earnings call.",
    )
    key_highlights: List[str] = Field(
        ..., description="List of key highlights mentioned during the earnings call."
    )


class StockPriceReaction(BaseModel):
    date: datetime = Field(
        ..., description="Date when the stock price reaction is recorded."
    )
    price_change: float = Field(
        ..., description="The change in stock price following the earnings call."
    )
    percentage_change: Optional[float] = Field(
        None, description="Percentage change in the stock price."
    )
    trading_volume: Optional[int] = Field(
        None, description="Trading volume of the stock following the earnings call."
    )


class EarningsCallTranscript(BaseModel):
    start_time: datetime = Field(..., description="Start time of the earnings call.")
    end_time: datetime = Field(..., description="End time of the earnings call.")
    transcript_text: str = Field(
        ..., description="Full transcript text of the earnings call."
    )
    participants: List[str] = Field(
        ..., description="List of participants in the earnings call."
    )


class EarningsCallAnalysis(BaseModel):
    transcript: EarningsCallTranscript = Field(
        ..., description="Detailed transcript of the earnings call."
    )
    financial_metrics: List[FinancialMetric] = Field(
        ..., description="List of key financial metrics discussed in the call."
    )
    analyst_questions: List[AnalystQuestion] = Field(
        ..., description="Questions from analysts and corresponding responses."
    )
    performance_summary: PerformanceSummary = Field(
        ..., description="Summary of the company's performance."
    )
    stock_price_reactions: List[StockPriceReaction] = Field(
        ..., description="Stock price reactions following the earnings call."
    )
