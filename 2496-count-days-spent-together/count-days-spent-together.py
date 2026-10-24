class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Number of days in each month for a non-leap year
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Helper function to convert "MM-DD" to day of the year (1-365)
        def date_to_day(date_str: str) -> int:
            month, day = map(int, date_str.split("-"))
            total_days = sum(days_in_months[:month - 1]) + day
            return total_days
        
        # Convert all four dates to day numbers
        a_arrive = date_to_day(arriveAlice)
        a_leave = date_to_day(leaveAlice)
        b_arrive = date_to_day(arriveBob)
        b_leave = date_to_day(leaveBob)
        
        # Calculate the intersection of the two date ranges
        overlap_start = max(a_arrive, b_arrive)
        overlap_end = min(a_leave, b_leave)
        
        # If overlap is valid, return the number of days; otherwise return 0
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        return 0