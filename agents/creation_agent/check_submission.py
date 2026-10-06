"""Supplement course checks for the object/string/array contracts in this scaffold."""
from pathlib import Path
import hashlib,json,subprocess,sys
root=Path(__file__).resolve().parents[2]
a=Path(__file__).resolve().parent
def validate(value,schema,path='root'):
 kind=schema.get('type')
 types={'object':dict,'array':list,'string':str}
 if kind in types and not isinstance(value,types[kind]): raise ValueError(path+': wrong type')
 if kind=='object':
  for key in schema.get('required',[]):
   if key not in value: raise ValueError(path+': missing '+key)
  if schema.get('additionalProperties') is False:
   if set(value)-set(schema.get('properties',{})): raise ValueError(path+': unexpected fields')
  for key,v in value.items():
   if key in schema.get('properties',{}): validate(v,schema['properties'][key],path+'.'+key)
 if kind=='array':
  for i,v in enumerate(value): validate(v,schema.get('items',{}),path+f'[{i}]')
logs=[]
for p in sorted((a/'cases').glob('*.json')):
 validate(json.loads(p.read_text()),json.loads((root/'core/input_schema.json').read_text()))
 logs.append(str(p.relative_to(root))+': intake field/type check PASS')
for p in sorted((a/'responses').glob('*.json')):
 result=subprocess.run([sys.executable,str(root/'tools/validate_response.py'),str(p)],capture_output=True,text=True,check=True)
 validate(json.loads(p.read_text()),json.loads((root/'core/output_schema.json').read_text()))
 logs.append(str(p.relative_to(root))+': '+result.stdout.strip()+'; nested field/type and unexpected top-level field check PASS')
result=subprocess.run([sys.executable,str(root/'tools/check_frozen_core.py')],capture_output=True,text=True,check=True)
logs.append(result.stdout.strip())
results=[json.loads((a/f'responses/{n}_response_v0_2.json').read_text()) for n in ['primary','contrast_1','contrast_2']]
hashes=[hashlib.sha256(x['general_et_finding'].encode()).hexdigest() for x in results]
assert len(set(hashes))==1
logs.append('General history SHA-256 identical across 3 contexts: '+hashes[0])
assert len(set(x['recommendation_management_implication'] for x in results))==3
logs.append('Three distinct contextual recommendations preserved; semantic review is recorded separately.')
original=json.loads((a/'prompts/primary_v0_1_prompt.txt').read_text().split('# CASE CONTEXT\n')[1].split('# REQUIRED OUTPUT SCHEMA')[0])
assert original==json.loads((a/'cases/primary.json').read_text())
logs.append('Primary case unchanged between baseline and revision: PASS')
text='# Validation results\n\nRun date: 2026-10-06. Unchanged course validator and integrity checker, with a supplementary standard-library contract checker for the schema keywords used here. This is not a general JSON Schema implementation.\n\n'+'\n\n'.join(logs)+'\n\nStructural checks do not establish factual accuracy or real-world performance. These are analytical outputs produced in this ChatGPT/Codex session; no separate API, hosted model, or production RAG application was run.\n'
(a/'records/validation_results.md').write_text(text)
print(text)
