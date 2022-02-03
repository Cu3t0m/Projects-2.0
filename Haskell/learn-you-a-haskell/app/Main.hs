module Main where

import Lib

-- Chapter 1: Starting out -> Used ghci
doubleMe x = x + x
-- doubleUs x y = x*2 + y*2 
doubleUs x y = doubleMe x + doubleMe y
doubleASmallNumber x = if x > 100
    then x
    else x*2
doubleSmallNumber' x = (if x > 100 then x else x*2) + 1


main :: IO ()
main = do
    putStrLn "Hello World!"