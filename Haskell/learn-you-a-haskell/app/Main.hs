module Main where

import Lib

doubleMe x = x + x
eighteen = doubleMe 9


main :: IO ()
main = do
    putStrLn "Hello World!"
    