from faker import Factory
from collections import defaultdict
import pandas as pd

def anonymize(source, target):
    
    # Read in source data
    df = pd.read_csv(source)
    
    # Create Faker instance
    faker  = Factory.create()
    
    # Create mappings of fields.
    names  = defaultdict(faker.name)
    emails = defaultdict(faker.email)
    ss = defaultdict(faker.ssn)
    phone = defaultdict(faker.phone_number)
    
    # Create copy of df
    anon_df = df
    
    # Update column names in brackets if customer's field names are different
    anon_df['name'] = anon_df['name'].map(names)  
    anon_df['email'] = anon_df['email'].map(emails)
    anon_df['ssn'] = anon_df['ssn'].map(ss) 
    anon_df['phone'] = anon_df['phone'].map(phone)

    # Export Anonymized data
    anon_df.to_csv(target)

if __name__ == "__main__":
    input_frame = input('What is the input file name (in CSV)? ')
    output_frame = input('What is the output file name (in CSV)? ')
    anonymize(input_frame, output_frame)