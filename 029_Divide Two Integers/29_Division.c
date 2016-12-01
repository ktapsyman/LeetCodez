#ifndef MAX_INT
#define MAX_INT INT_MAX
#endif

int PositiveDivide( unsigned int dividend, unsigned int divisor )
{
    int Q = 0;
	while (dividend >= divisor)
	{
		unsigned int ShiftedDividend = dividend;
		unsigned int ShiftedBit = 0;
		while (divisor <= ShiftedDividend)
		{
			ShiftedDividend >>= 1;
			ShiftedBit++;
		}
		--ShiftedBit;
		dividend -= (divisor << ShiftedBit);
		Q |= (1 << ShiftedBit);
	}
	return Q;
}

int divide(int dividend, int divisor) 
{
    if( !divisor || !dividend )return 0;
    if( dividend == divisor )return 1;
    if( dividend == INT_MAX && abs(divisor) == 1 )return (abs(divisor) == divisor) ? MAX_INT : -2147483647;
    if( abs(dividend) < 0 && abs(divisor) == 1 )return (abs(divisor) == divisor) ?  -2147483648 : MAX_INT;
    int ret = 0;
    unsigned int OverflowDividend = abs(dividend) < 0 ? INT_MAX+1 : dividend;
    if( dividend > 0 && divisor > 0 || dividend < 0 && divisor < 0 )
    {
        if( dividend < 0 && abs(dividend) < 0)
            ret += PositiveDivide(OverflowDividend, abs(divisor));
        else
            ret += PositiveDivide(abs(dividend), abs(divisor));
    }
    else
    {
        if( dividend < 0 && abs(dividend) < 0)
            ret -= PositiveDivide(OverflowDividend, abs(divisor));
        else
            ret -= PositiveDivide(abs(dividend), abs(divisor));
    }
    return ret;
}
