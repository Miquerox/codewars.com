<?php

// https://www.codewars.com/kata/563e320cee5dddcf77000158/train/php

function get_average($a)
{
    return intval(floor(array_sum($a) / count($a)));
}
