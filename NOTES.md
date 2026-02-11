## MY ASSUMPTIONS

## Task 1 — Average Order Value
- **Order amount values may be positive, negative, or zero.**  
  A zero average is therefore considered a valid result when there are valid (non-cancelled) orders. To avoid conflating this with the absence of data, the function returns `None` only when no valid orders exist.

- **Order amounts are expected to be real numeric values in the data schema.**  
  Non-numeric or malformed amount values are treated as invalid and skipped, rather than being implicitly coerced, to keep the data contract explicit.

- **Average Order Value is assumed to be computed over non-cancelled orders only.**  
  Although the AI-generated implementation did not fully achieve this, its intent is clear from both the code and explanation, and the corrected implementation aligns with this intended behavior.

## Task 2 — Count Valid Emails

- **Pragmatic email validation was chosen.**  
  A simplified regular expression is used instead of full RFC-compliant validation, as stricter validation was considered out of scope for this task.

- **Fail-safe behavior was preferred over raising exceptions.**  
  Invalid or malformed inputs are handled safely to prevent runtime crashes and ensure predictable behavior.

- **Non-string entries are safely ignored.**  
  Elements that are not strings are skipped instead of causing the function to fail.

- **Whitespace is handled explicitly.**  
  Leading and trailing whitespace is stripped before validation to avoid false negatives.

- **Validation scope is limited to syntax only.**  
  The function checks only the structural format of email addresses and does not verify domain existence or deliverability.

## Task 3 — Aggregate Valid Measurements

- **Input is expected to be a list or tuple.**  
  If the input is not a list or tuple, the function returns None rather than attempting to process invalid data.

- **Only values that can be safely converted to numeric form are considered valid measurements.**  
  Measurements are treated as valid if they can be converted using `float`; values that raise `TypeError` or `ValueError` are excluded.

- **`None` explicitly represents missing data.**  
  `None` values are skipped and do not contribute to either the sum or the count.

- **Implicit numeric conversion is acceptable for this domain.**  
  Allowing conversion via `float` supports common real-world data sources such as CSV or JSON, where numeric values may be represented as strings.

- **Returning `None` signals the absence of meaningful data.**  
  If no valid measurements exist after filtering, the function returns `None` to distinguish “no data” from a valid average of `0`.

- **Negative and zero values are considered valid measurements.**  
  The function does not restrict the sign of numeric values, assuming that negative or zero measurements may be meaningful depending on the domain.

- **Locale-specific numeric formats are not normalized.**  
  Conversions such as `"2,3"` → `"2.3"` are intentionally not handled, as locale-dependent normalization is assumed to be the responsibility of data ingestion or preprocessing layers.